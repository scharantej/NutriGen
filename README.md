## Flask Application Design for AI-Based Recipe and Meal Planning Service - PlatefulAI

### HTML Files

- **profile.html**: Displays the user's profile, including their dietary preferences, restrictions, and nutritional goals. Provides an interface for users to edit their profile.
- **mealplan.html**: Displays the generated meal plan based on the user's profile. Includes recipes, nutritional information, and meal notes.
- **recipes.html**: Lists all recipes available in the database, with options to filter based on dietary preferences and nutritional needs.
- **search.html**: Allows users to search for specific recipes by name, ingredients, or dietary compatibility.

### Routes

- **@app.route('/profile')**: Renders the profile.html page.
- **@app.route('/update_profile', methods=['POST'])**: Handles POST requests from the profile.html page, updating the user's preferences, restrictions, and goals.
- **@app.route('/mealplan')**: Generates a personalized meal plan based on the user's profile and renders the mealplan.html page.
- **@app.route('/recipes')**: Renders the recipes.html page with a list of all available recipes.
- **@app.route('/search')**: Renders the search.html page with a form for searching recipes.
- **@app.route('/search_recipes', methods=['POST'])**: Handles POST requests from the search.html page, performing the recipe search and returning results.