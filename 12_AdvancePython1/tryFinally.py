def main():

    try:
        a = int(input("Hey enter a number : "))
        print(a)

    except Exception as e:
        print(e)
# it is used in functions so that this block always works
    finally:
        print("I am inside else")  # it always works whether try is successful or not

main()