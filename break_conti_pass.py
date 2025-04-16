# Example showing all three:
for i in range(1, 6):
    if i == 1:
        continue  # Skips 1
    elif i == 3:
        pass      # Does nothing (3 gets printed)
    elif i == 5:
        break     # Loop ends before 5
    print(i)
# Output: 2 3 4

### IMPORTANT NOTES:
# 1. break vs continue:
#    - break: "I'm done with this loop entirely"
#    - continue: "Skip this item but keep looping"

# 2. pass vs continue:
#    - pass: "No action needed here" (structural placeholder)
#    - continue: Actively skips iteration (control flow)

# 3. Performance:
#    - All three have negligible runtime cost
#    - break can improve performance by exiting early

# 4. Code Readability:
#    - Multiple continue statements can make logic hard to follow
#    - break is often clearer than complex loop conditions 