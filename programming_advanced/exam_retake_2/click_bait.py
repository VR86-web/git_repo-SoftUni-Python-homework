from collections import deque

suggested_links = deque([int(x) for x in input().split()])
featured_articles = [int(x) for x in input().split()]
target_engagement_value = int(input())

final_feed = []

while suggested_links and featured_articles:

    fifo_element = suggested_links.popleft()

    lifo_element = featured_articles.pop()

    if fifo_element > lifo_element:
        greater, smaller = fifo_element, lifo_element
        origin = "FIFO"
    elif lifo_element > fifo_element:
        greater, smaller = lifo_element, fifo_element
        origin = "LIFO"
    else:
        final_feed.append(0)
        continue

    remainder = greater % smaller

    if origin == "LIFO":
        final_feed.append(remainder)
        if remainder != 0:
            featured_articles.append(remainder * 2)
    elif origin == "FIFO":
        final_feed.append(-remainder)
        if remainder != 0:
            suggested_links.append(remainder * 2)

total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join(map(str, final_feed))}")

if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    shortfall = target_engagement_value - total_engagement_value
    print(f"Goal not achieved! Short by: {shortfall}")

