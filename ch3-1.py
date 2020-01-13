bycycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bycycles)
print(bycycles[0])
print(bycycles[2].title())
print(bycycles[-1].title()) # Index -1 always return the last item on the list
print(bycycles[-2].title()) # Index -2 returns the second item from the end of the list

message = f"My first bicycle was a {bycycles[0].title()}"
print(message)
