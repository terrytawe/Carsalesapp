
# ────────────────────────────────────────────────────────────────────────────────────────────────
# Function to get cleaned data from form
# ────────────────────────────────────────────────────────────────────────────────────────────────

def get_POST(request, field, default=''):
    return request.POST.get(field, default).strip()