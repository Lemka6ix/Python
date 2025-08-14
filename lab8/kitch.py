import dearpygui.dearpygui as dpg
from typing import List, Dict, Set
import json
import os


class RecipeError(Exception):
    """Base exception for recipe errors"""
    pass


class RecipeNotFoundError(RecipeError):
    """Exception for when recipe is not found"""
    pass


class InvalidIngredientError(RecipeError):
    """Exception for invalid ingredients"""
    pass


class Recipe:
    """Class representing a recipe"""
    def __init__(self, name: str, ingredients: List[str], instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def to_dict(self) -> Dict:
        """Converts recipe to dictionary for serialization"""
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Recipe':
        """Creates recipe from dictionary"""
        return cls(
            name=data["name"],
            ingredients=data["ingredients"],
            instructions=data["instructions"]
        )
    
    def matches_ingredients(self, ingredients: Set[str]) -> bool:
        """Checks if recipe contains all specified ingredients"""
        return all(ingredient.lower() in {i.lower() for i in self.ingredients} 
                  for ingredient in ingredients)


class RecipeCatalog:
    """Class for managing recipe catalog"""
    def __init__(self):
        self.recipes: List[Recipe] = []
        self.load_recipes()
    
    def add_recipe(self, recipe: Recipe):
        """Adds recipe to catalog"""
        if not recipe.name or not recipe.ingredients:
            raise InvalidIngredientError("Recipe name and ingredients are required")
        self.recipes.append(recipe)
        self.save_recipes()
    
    def remove_recipe(self, recipe_name: str):
        """Removes recipe from catalog"""
        recipe = self.find_recipe(recipe_name)
        if recipe:
            self.recipes.remove(recipe)
            self.save_recipes()
        else:
            raise RecipeNotFoundError(f"Recipe '{recipe_name}' not found")
    
    def find_recipe(self, recipe_name: str) -> Recipe:
        """Finds recipe by name"""
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None
    
    def find_recipes_by_ingredients(self, ingredients: List[str]) -> List[Recipe]:
        """Finds recipes containing all specified ingredients"""
        if not ingredients:
            raise InvalidIngredientError("At least one ingredient must be specified")
        
        ingredient_set = {i.strip().lower() for i in ingredients if i.strip()}
        return [recipe for recipe in self.recipes 
                if recipe.matches_ingredients(ingredient_set)]
    
    def save_recipes(self):
        """Saves recipes to file"""
        with open("recipes.json", "w", encoding="utf-8") as f:
            json.dump([recipe.to_dict() for recipe in self.recipes], f, ensure_ascii=False, indent=2)
    
    def load_recipes(self):
        """Loads recipes from file"""
        if os.path.exists("recipes.json"):
            with open("recipes.json", "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    self.recipes = [Recipe.from_dict(item) for item in data]
                except json.JSONDecodeError:
                    self.recipes = []


class RecipeApp:
    """GUI application class for recipe catalog"""
    def __init__(self):
        self.catalog = RecipeCatalog()
        self.selected_recipe = None
        self.current_ingredients = []
        
        dpg.create_context()
        self.setup_ui()
        dpg.create_viewport(title='Recipe Catalog', width=800, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def setup_ui(self):
        """Sets up user interface"""
        # Add recipe window
        with dpg.window(label="Add Recipe", tag="add_recipe_window", width=400, height=400, pos=[50, 50]):
            dpg.add_input_text(label="Recipe Name", tag="recipe_name")
            
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Ingredient", tag="new_ingredient", width=200)
                dpg.add_button(label="Add", callback=self.add_ingredient)
            
            dpg.add_text("Ingredients:")
            dpg.add_listbox(tag="ingredients_list", items=[], width=300, num_items=5)
            dpg.add_button(label="Remove Ingredient", callback=self.remove_ingredient)
            
            dpg.add_input_text(label="Instructions", tag="instructions", multiline=True, height=150, width=300)
            dpg.add_button(label="Save Recipe", callback=self.save_recipe)
        
        # Search recipes window
        with dpg.window(label="Search Recipes", tag="search_window", width=400, height=400, pos=[500, 50]):
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Search Ingredient", tag="search_ingredient", width=200)
                dpg.add_button(label="Add", callback=self.add_search_ingredient)
            
            dpg.add_text("Search by ingredients:")
            dpg.add_listbox(tag="search_ingredients_list", items=[], width=300, num_items=5)
            dpg.add_button(label="Remove Ingredient", callback=self.remove_search_ingredient)
            dpg.add_button(label="Find Recipes", callback=self.search_recipes)
            
            dpg.add_text("Found Recipes:")
            dpg.add_listbox(tag="found_recipes_list", items=[], width=300, num_items=5,
                          callback=self.select_found_recipe)
            
            dpg.add_button(label="Delete Recipe", callback=self.delete_recipe)
        
        # View recipe window
        with dpg.window(label="View Recipe", tag="view_recipe_window", width=600, height=400, pos=[100, 500], show=False):
            dpg.add_text("", tag="view_recipe_name")
            dpg.add_text("Ingredients:", tag="view_recipe_ingredients_label")
            dpg.add_text("", tag="view_recipe_ingredients", bullet=True)
            dpg.add_text("Instructions:", tag="view_recipe_instructions_label")
            dpg.add_text("", tag="view_recipe_instructions")
    
    def add_ingredient(self, sender, app_data):
        """Adds ingredient to new recipe"""
        ingredient = dpg.get_value("new_ingredient")
        if ingredient:
            current = dpg.get_value("ingredients_list")
            current.append(ingredient)
            dpg.set_value("ingredients_list", current)
            dpg.set_value("new_ingredient", "")
    
    def remove_ingredient(self, sender, app_data):
        """Removes ingredient from new recipe"""
        selected = dpg.get_value("ingredients_list")
        current = dpg.get_value("ingredients_list")
        if selected in current:
            current.remove(selected)
            dpg.set_value("ingredients_list", current)
    
    def save_recipe(self, sender, app_data):
        """Saves new recipe"""
        try:
            name = dpg.get_value("recipe_name")
            ingredients = dpg.get_value("ingredients_list")
            instructions = dpg.get_value("instructions")
            
            if not name:
                raise InvalidIngredientError("Enter recipe name")
            if not ingredients:
                raise InvalidIngredientError("Add at least one ingredient")
            
            recipe = Recipe(name, ingredients, instructions)
            self.catalog.add_recipe(recipe)
            
            # Clear fields
            dpg.set_value("recipe_name", "")
            dpg.set_value("ingredients_list", [])
            dpg.set_value("instructions", "")
            dpg.set_value("new_ingredient", "")
            
            dpg.configure_item("modal_window", show=False)
        except RecipeError as e:
            self.show_error(str(e))
    
    def add_search_ingredient(self, sender, app_data):
        """Adds search ingredient"""
        ingredient = dpg.get_value("search_ingredient")
        if ingredient:
            current = dpg.get_value("search_ingredients_list")
            current.append(ingredient)
            dpg.set_value("search_ingredients_list", current)
            dpg.set_value("search_ingredient", "")
    
    def remove_search_ingredient(self, sender, app_data):
        """Removes search ingredient"""
        selected = dpg.get_value("search_ingredients_list")
        current = dpg.get_value("search_ingredients_list")
        if selected in current:
            current.remove(selected)
            dpg.set_value("search_ingredients_list", current)
    
    def search_recipes(self, sender, app_data):
        """Searches recipes by ingredients"""
        try:
            ingredients = dpg.get_value("search_ingredients_list")
            recipes = self.catalog.find_recipes_by_ingredients(ingredients)
            dpg.set_value("found_recipes_list", [recipe.name for recipe in recipes])
        except RecipeError as e:
            self.show_error(str(e))
    
    def select_found_recipe(self, sender, app_data):
        """Selects recipe from found list"""
        recipe_name = dpg.get_value("found_recipes_list")
        if recipe_name:
            recipe = self.catalog.find_recipe(recipe_name)
            if recipe:
                self.show_recipe(recipe)
    
    def show_recipe(self, recipe: Recipe):
        """Shows recipe details"""
        dpg.set_value("view_recipe_name", f"Recipe: {recipe.name}")
        
        # Format ingredients
        ingredients_text = "\n".join(recipe.ingredients)
        dpg.set_value("view_recipe_ingredients", ingredients_text)
        
        dpg.set_value("view_recipe_instructions", recipe.instructions)
        dpg.show_item("view_recipe_window")
    
    def delete_recipe(self, sender, app_data):
        """Deletes selected recipe"""
        recipe_name = dpg.get_value("found_recipes_list")
        if recipe_name:
            try:
                self.catalog.remove_recipe(recipe_name)
                # Update found recipes list
                ingredients = dpg.get_value("search_ingredients_list")
                if ingredients:
                    recipes = self.catalog.find_recipes_by_ingredients(ingredients)
                    dpg.set_value("found_recipes_list", [recipe.name for recipe in recipes])
                else:
                    dpg.set_value("found_recipes_list", [])
                
                dpg.hide_item("view_recipe_window")
            except RecipeError as e:
                self.show_error(str(e))
    
    def show_error(self, message: str):
        """Shows error message"""
        with dpg.window(label="Error", modal=True, show=True, tag="modal_window", 
                       no_title_bar=True, width=300, height=100):
            dpg.add_text(message)
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.configure_item("modal_window", show=False))


if __name__ == "__main__":
    app = RecipeApp()