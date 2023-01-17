class myclass:
    a = 5
    b = "ads"
    c = [1, 3, 5]

    def write(self):
        d = 100
        print(d, self.a)

    def write2(self, t):
        self.write()
        print(t)


nesne = myclass()
nesne.yazdir()
nesne.yazdir2("lkjhgfdkjh")
