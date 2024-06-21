delay_times = [10, 10, 10, 0, 0, 5]
total_delay = sum(delay_times)
num_flights = len(delay_times)
avg_delay = total_delay/num_flights
print(avg_delay)