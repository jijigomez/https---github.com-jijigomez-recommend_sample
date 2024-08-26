from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Tour





from django.shortcuts import render
from .models import Tour, UserProfile  # Assuming these models are defined
import pandas as pd
from .recommendation import recommend_tours  # Import the recommendation function

def tour_list(request):
    """View to list all available tours."""
    tours = Tour.objects.all()  # Retrieve all tours from the database
    return render(request, 'tour_list.html', {'tours': tours})

def recommended_tours(request):
    """View to generate and display recommended tours based on user search input."""
    
    # Sample data as before
    data = {
        'TourID': [1, 2, 3, 4, 5,],
        'Name': ['Paris Adventure', 'London Royal Experience', 'New York City Highlights', 'Tokyo Cultural Tour', 'Sydney Coastal Escape'],
        'Location': ['Paris', 'London', 'New York', 'Tokyo', 'Sydney'],
        'Description': [
            'Explore the city of lights with guided tours to iconic landmarks like the Eiffel Tower and the Louvre.',
            'A royal tour of London\'s historical sites including Buckingham Palace and the Tower of London.',
            'Discover the Big Apple with visits to Times Square, Central Park, and the Statue of Liberty.',
            'Experience the rich culture of Tokyo with a mix of traditional and modern attractions.',
            'Enjoy the beauty of Sydney with beach visits, harbour cruises, and the Sydney Opera House.',
        ],
        'Price': [1500.00, 1800.00, 2000.00, 2200.00, 1700.00]
    }

    all_tours = pd.DataFrame(data)  # Create a pandas DataFrame

    # Get search query from the request
    search_query = request.GET.get('search', '')

    if search_query:
        # Filter tours based on the search query (e.g., by location or name)
        filtered_tours = all_tours[all_tours['Location'].str.contains(search_query, case=False)]
    else:
        # No search query, show all tours
        filtered_tours = all_tours

    # Sample user profile (as an example)
    user_profile = {
        'interests': ['culture', 'history', 'sightseeing'],
        'budget': 2000
    }

    # Get recommendations based on the filtered tours
    recommendations = recommend_tours(user_profile, filtered_tours)

    # Convert recommendations to a list of dictionaries
    recommended_tours_list = recommendations.to_dict('records')

    return render(request, 'recommended_tours.html', {'tours': recommended_tours_list})
