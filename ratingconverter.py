'''def starRating(rating):
    stars = ''

    # Check if the rating is within the valid range
    if 1 <= rating <= 5:
        # Append full stars
        stars += '★' * int(rating)

        # If the rating has a decimal part, append a half star
        if rating % 1 != 0:
            stars += '½'

        # Append remaining empty stars to make a total of 5 stars
        stars += '☆' * (5 - int(rating))

    else:
        stars = 'Invalid rating'

    return stars

# Example usage:
print(starRating(3.5))  # Output: "★★★½☆"'''

def starRating(rating):
    # Convert the rating to a numerical type (float or int)
    rating = float(rating)
    
    stars = ''

    # Check if the rating is within the valid range
    if 1 <= rating <= 5:
        # Append full stars
        stars += '★' * int(rating)

        # If the rating has a decimal part, append a half star
        if rating % 1 != 0:
            stars += '½'

        # Append remaining empty stars to make a total of 5 stars
        stars += '☆' * (5 - int(rating))

    else:
        stars = 'Invalid rating'

    return stars

# Example usage:
print(starRating("3.5"))  # Output: "★★★½☆"
