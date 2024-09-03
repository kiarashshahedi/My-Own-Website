from django.shortcuts import render

def buyer_dashboard(request):
    # Fetch user-related data like shopping history, account info, etc.
    context = {
        'user': request.user,
        # Additional context data as needed
    }
    return render(request, 'accounts/buyer_dashboard.html', context)