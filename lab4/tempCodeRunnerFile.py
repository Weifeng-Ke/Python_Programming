#ensure every thread is finished before computing the time
for i in threads:
    i.join()