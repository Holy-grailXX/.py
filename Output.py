def output(self):
        h = self.head
        while h is not None:
            print(h.data, end=" ")
            h = h.next
        print()
