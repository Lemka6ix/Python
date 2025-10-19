import dearpygui.dearpygui as dpg
from typing import List, Dict, Set
import json
import os


class RecipeError(Exception):
    """Исключение для ошибок рецептов"""
    pass


class RecipeNotFoundError(RecipeError):
    """Исключение, когда рецепт не найден"""
    pass


class InvalidIngredientError(RecipeError):
    """Исключение для недопустимых ингредиентов"""
    pass


class Recipe:

    def __init__(self, name: str, ingredients: List[str], instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
    
    def to_dict(self) -> Dict:
        """Рецепт в словарь"""
        return {
            "name": self.name,
            "ingredients": self.ingredients,
            "instructions": self.instructions
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Recipe':
        """Создает рецепт из словаря"""
        return cls(
            name=data["name"],
            ingredients=data["ingredients"],
            instructions=data["instructions"]
        )
    
    def matches_ingredients(self, search_ingredients: Set[str]) -> bool:
        """Проверяет содержит ли рецепт все указанные ингредиенты"""
        if not search_ingredients:
            return False
        
        recipe_ingredients = {i.lower().strip() for i in self.ingredients}
        search_ingredients_lower = {i.lower().strip() for i in search_ingredients}
        
        return search_ingredients_lower.issubset(recipe_ingredients)


class RecipeCatalog:
    """Класс для управления котологом рецептов"""
    def __init__(self):
        self.recipes: List[Recipe] = []
        self.load_recipes()
    
    def add_recipe(self, recipe: Recipe):
        """добавляет рецепт в каталог"""
        if not recipe.name or not recipe.ingredients:
            raise InvalidIngredientError("Recipe name and ingredients are required")
        self.recipes.append(recipe)
        self.save_recipes()
    
    def remove_recipe(self, recipe_name: str):
        """удаляет рецепт из каталога"""
        recipe = self.find_recipe(recipe_name)
        if recipe:
            self.recipes.remove(recipe)
            self.save_recipes()
        else:
            raise RecipeNotFoundError(f"Recipe '{recipe_name}' not found")
    
    def find_recipe(self, recipe_name: str) -> Recipe:
        """Находит рецепт по имени"""
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None
    
    def find_recipes_by_ingredients(self, ingredients: List[str]) -> List[Recipe]:
        """Находит рецепты содержащие все указанные ингредиенты"""
        if not ingredients:
            raise InvalidIngredientError("At least one ingredient must be specified")
        
        ingredient_set = {i.strip() for i in ingredients if i.strip()}
        if not ingredient_set:
            raise InvalidIngredientError("At least one valid ingredient must be specified")
        
        return [recipe for recipe in self.recipes 
                if recipe.matches_ingredients(ingredient_set)]
    
    def save_recipes(self):
        """Сохранение рецепта в файл"""
        with open("recipes.json", "w", encoding="utf-8") as f:
            json.dump([recipe.to_dict() for recipe in self.recipes], f, ensure_ascii=False, indent=2)
    
    def load_recipes(self):
        """загружает рецепты из файла"""
        if os.path.exists("recipes.json"):
            try:
                with open("recipes.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.recipes = [Recipe.from_dict(item) for item in data]
            except (json.JSONDecodeError, FileNotFoundError):
                self.recipes = []
        else:
            self.recipes = []


class RecipeApp:
    """GUI класс для каталога рецептов"""
    def __init__(self):
        self.catalog = RecipeCatalog()
        self.selected_recipe = None
        self.new_recipe_ingredients = []
        self.search_ingredients = []
        self.found_recipes = []
        
        dpg.create_context()
        self.setup_ui()
        dpg.create_viewport(title='Recipe Catalog', width=1300, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    def setup_ui(self):
        """UI настройка"""
        # Окно "Add recipe"
        with dpg.window(label="Add Recipe", tag="add_recipe_window", width=400, height=400, pos=[50, 50]):
            dpg.add_input_text(label="Recipe Name", tag="recipe_name")
            
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Ingredient", tag="new_ingredient", width=200)
                dpg.add_button(label="Add", callback=self.add_ingredient)
            
            dpg.add_text("Ingredients:")
            dpg.add_listbox(tag="ingredients_list", items=self.new_recipe_ingredients, width=300, num_items=5)
            dpg.add_button(label="Remove Selected", callback=self.remove_ingredient)
            
            dpg.add_input_text(label="Instructions", tag="instructions", multiline=True, height=150, width=300)
            dpg.add_button(label="Save Recipe", callback=self.save_recipe)
        
        # Окно "Search recipes"
        with dpg.window(label="Search Recipes", tag="search_window", width=400, height=400, pos=[500, 50]):
            with dpg.group(horizontal=True):
                dpg.add_input_text(label="Search Ingredient", tag="search_ingredient", width=200)
                dpg.add_button(label="Add", callback=self.add_search_ingredient)
            
            dpg.add_text("Search by ingredients:")
            dpg.add_listbox(tag="search_ingredients_list", items=self.search_ingredients, width=300, num_items=5)
            dpg.add_button(label="Remove Selected", callback=self.remove_search_ingredient)
            dpg.add_button(label="Find Recipes", callback=self.search_recipes)
            
            dpg.add_text("Found Recipes:")
            dpg.add_listbox(tag="found_recipes_list", items=self.found_recipes, width=300, num_items=5,
                          callback=self.select_found_recipe)
            
            dpg.add_button(label="Delete Selected", callback=self.delete_recipe)
        
        # Оно "View recipe"
        with dpg.window(label="View Recipe", tag="view_recipe_window", width=300, height=400, pos=[950, 50], show=False):
            dpg.add_text("", tag="view_recipe_name")
            dpg.add_text("Ingredients:", tag="view_recipe_ingredients_label")
            dpg.add_text("", tag="view_recipe_ingredients", bullet=True)
            dpg.add_text("Instructions:", tag="view_recipe_instructions_label")
            dpg.add_text("", tag="view_recipe_instructions")
    
    def add_ingredient(self, sender, app_data):
        """Adds ingredient to new recipe"""
        ingredient = dpg.get_value("new_ingredient")
        if ingredient and ingredient.strip():
            self.new_recipe_ingredients.append(ingredient.strip())
            dpg.configure_item("ingredients_list", items=self.new_recipe_ingredients)
            dpg.set_value("new_ingredient", "")
    
    def remove_ingredient(self, sender, app_data):
        """Removes ingredient from new recipe"""
        selected = dpg.get_value("ingredients_list")
        if selected and selected in self.new_recipe_ingredients:
            self.new_recipe_ingredients.remove(selected)
            dpg.configure_item("ingredients_list", items=self.new_recipe_ingredients)
    
    def save_recipe(self, sender, app_data):
        """Saves new recipe"""
        try:
            name = dpg.get_value("recipe_name")
            instructions = dpg.get_value("instructions")
            
            if not name or not name.strip():
                raise InvalidIngredientError("Enter recipe name")
            if not self.new_recipe_ingredients:
                raise InvalidIngredientError("Add at least one ingredient")
            
            recipe = Recipe(name.strip(), self.new_recipe_ingredients.copy(), instructions.strip())
            self.catalog.add_recipe(recipe)
            
            # Clear fields
            dpg.set_value("recipe_name", "")
            self.new_recipe_ingredients = []
            dpg.configure_item("ingredients_list", items=[])
            dpg.set_value("instructions", "")
            dpg.set_value("new_ingredient", "")
            
        except RecipeError as e:
            self.show_error(str(e))
    
    def add_search_ingredient(self, sender, app_data):
        """Adds search ingredient"""
        ingredient = dpg.get_value("search_ingredient")
        if ingredient and ingredient.strip():
            self.search_ingredients.append(ingredient.strip())
            dpg.configure_item("search_ingredients_list", items=self.search_ingredients)
            dpg.set_value("search_ingredient", "")
    
    def remove_search_ingredient(self, sender, app_data):
        """Removes search ingredient"""
        selected = dpg.get_value("search_ingredients_list")
        if selected and selected in self.search_ingredients:
            self.search_ingredients.remove(selected)
            dpg.configure_item("search_ingredients_list", items=self.search_ingredients)
    
    def search_recipes(self, sender, app_data):
        """Searches recipes by ingredients"""
        try:
            recipes = self.catalog.find_recipes_by_ingredients(self.search_ingredients)
            self.found_recipes = [recipe.name for recipe in recipes]
            dpg.configure_item("found_recipes_list", items=self.found_recipes)
            
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
        
        ingredients_text = "\n".join([f"• {ingredient}" for ingredient in recipe.ingredients])
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
                if self.search_ingredients:
                    recipes = self.catalog.find_recipes_by_ingredients(self.search_ingredients)
                    self.found_recipes = [recipe.name for recipe in recipes]
                    dpg.configure_item("found_recipes_list", items=self.found_recipes)
                else:
                    self.found_recipes = []
                    dpg.configure_item("found_recipes_list", items=[])
                
                dpg.hide_item("view_recipe_window")
            except RecipeError as e:
                self.show_error(str(e))
    
    def show_error(self, message: str):
        """Shows error message"""
        if dpg.does_item_exist("error_modal"):
            dpg.delete_item("error_modal")
        
        with dpg.window(label="Error", modal=True, show=True, tag="error_modal", 
                       no_title_bar=True, width=300, height=100, pos=[250, 250]):
            dpg.add_text(message)
            dpg.add_button(label="OK", width=75, callback=lambda: dpg.delete_item("error_modal"))


if __name__ == "__main__":
    app = RecipeApp()