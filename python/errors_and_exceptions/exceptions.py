N = int(input())
for _ in range(N):
    input = input().split(' ')
    try:
        print(int(input[0])//int(input[1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
    finally:
    	del input
