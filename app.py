import gradio as gr

# Define the mapping of unhealthy ingredients to healthier alternatives
ingredient_swaps = {
    "white rice": "brown rice or quinoa",
    "white pasta": "whole grain or lentil pasta",
    "sour cream": "low-fat Greek yogurt",
    "whole milk": "almond milk or oat milk",
    "mayonnaise": "mashed avocado",
    "white flour": "almond flour or oat flour",
    "bottled dressing": "olive oil and lemon juice",
    "butter": "olive oil or avocado oil",
    "sugar": "honey or stevia",
    "salt": "herbs or spices",
    "cream": "coconut cream or low-fat yogurt",
    "cheddar cheese": "low-fat cheese or nutritional yeast",
    "fried chicken": "grilled chicken or baked tofu",
    "potato chips": "baked sweet potato chips or kale chips",
    "ice cream": "frozen banana or Greek yogurt-based dessert"
}

# Function to suggest healthier swaps
def suggest_swaps(recipe_text):
    suggestions = []
    recipe_lower = recipe_text.lower()
    for ingredient, substitute in ingredient_swaps.items():
        if ingredient in recipe_lower:
            suggestions.append(f"Swap '{ingredient}' with '{substitute}'.")
    if suggestions:
        return "\n".join(suggestions)
    else:
        return "No unhealthy ingredients detected. Your recipe looks great!"

# Create Gradio interface
demo = gr.Interface(
    fn=suggest_swaps,
    inputs=gr.Textbox(lines=10, placeholder="Paste your recipe here..."),
    outputs="text",
    title="Healthy Recipe Swaps Generator",
    description="Paste your recipe to get healthier ingredient alternatives."
)

# Launch the app
demo.launch()
