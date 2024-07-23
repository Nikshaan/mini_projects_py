# PIGLATIN

message = input("Enter your message: ")

for i in range(len(message)):  # each word in message
    if message[i].lower() in 'aeiou':
        x = i
        break

print(message[x:] + message[:x] + 'ay')
