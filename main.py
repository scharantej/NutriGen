
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/update_profile', methods=['POST'])
def update_profile():
    preferences = request.form.getlist('preferences')
    restrictions = request.form.getlist('restrictions')
    goals = request.form.getlist('goals')
    return render_template('profile.html', preferences=preferences, restrictions=restrictions, goals=goals)

@app.route('/mealplan')
def mealplan():
    preferences = request.form.getlist('preferences')
    restrictions = request.form.getlist('restrictions')
    goals = request.form.getlist('goals')
    recipes = pd.read_csv('recipes.csv')
    mealplan = generate_mealplan(preferences, restrictions, goals, recipes)
    return render_template('mealplan.html', mealplan=mealplan)

@app.route('/recipes')
def recipes():
    recipes = pd.read_csv('recipes.csv')
    return render_template('recipes.html', recipes=recipes)

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search_recipes', methods=['POST'])
def search_recipes():
    search_term = request.form['search_term']
    recipes = pd.read_csv('recipes.csv')
    results = recipes[recipes['name'].str.contains(search_term)]
    return render_template('recipes.html', recipes=results)

if __name__ == '__main__':
    app.run(debug=True)
