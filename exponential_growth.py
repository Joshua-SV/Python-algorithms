def exponential_growth(n, factor, days):
    expected_followers = [n,]

    for day in range(1,days+1):
        # growth is based on the equation initial * ratio^time
        followers = n * (factor ** day)
        expected_followers.append(followers)
    return expected_followers