if __name__ == '__main__':
    initial = 100
    rate_percent = 9.8
    periods = 8
    
    final = initial * (rate_percent/100 + 1)**periods
    
    print(final)
