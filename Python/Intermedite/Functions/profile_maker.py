def build_profile(first_name, last_name, **extra_info):
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }

    # Baqi saari extra details ko profile dictionary mein add karna
    profile.update(extra_info)
    return profile


# User ka profile banate hain jisme hum mazeed info bhi de rahe hain
my_profile = build_profile("Zeeshan", "Ahmed", role="Teacher", experience="3 Years", city="Hyderabad")
print(my_profile)