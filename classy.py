class duck:
    q = "Quaaaaak!!!"
    def sound(self):
        print (self.q)

    def walk(self):
        print("walks on 2 legs")

def main():
    Don = duck()
    Don.sound()
    Don.walk()
    print(Don.q)
    print(type(Don))
    print(type(Don.q))  
if __name__ == "__main__":
    main()