
class NodePelanggan:
    def __init__(self, namaPelanggan):
        self._namaPelanggan = namaPelanggan
     
    def getNamaPelanggan(self):
        return self._namaPelanggan
    
    def setnamaPelanggan(self, namaPelangganBaru):
        self._namaPelanggan = namaPelangganBaru
        

class Kasir:
    DEFAULT_CAPACITY = 3 #isi sesuai dengan ketentuan soal
    def __init__(self): #konstruktor
        self._data = []
        self._size = 0
        self.front = 0
       
    def __len__(self): #mengembalikan ukuran Queue
        return self._size

    def is_empty(self): #mengecek apakah Queue kosong ?
        return self._size == 0

    def dequeue(self): #menghapus data paling depan (front)
        data = self._data[0]
        print(f"### Pelanggan {data} Selesai Membayar ###")
        print()
        self._data.remove(data)
        self._data.append("Kosong")
        self._size -=1
        return data

    def enqueue(self, namaPelanggan): #menambah data ke list
        self._data.insert(self._size,namaPelanggan)
        if self._data[-1] == "Kosong":
            del self._data[-1]
        if self.DEFAULT_CAPACITY < len(self._data):
            self.resize(self.DEFAULT_CAPACITY)
        self._size +=1
    def resize(self, cap): #mengubah ukuran queue pada list
        print("### Melakukan Resize ###\n")
        for i in range(cap-1):
            self._data.append("Kosong")
        self.DEFAULT_CAPACITY = self.DEFAULT_CAPACITY * 2
    
    def printAll(self): #menampilkan daftar pelanggan dalam sebuah kasir
        #print(self._data)
        print("=== Kasir ===")
        for i in range (0,len(self._data)):
            print(str(i+1)+'. '+self._data[i])
        print()
        

# test case program
tempatKasir = Kasir()
tempatKasir.enqueue("Haniif")
tempatKasir.enqueue("Sindu")
tempatKasir.enqueue("Dedi")
tempatKasir.printAll()

tempatKasir.enqueue("Beatrix")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

tempatKasir.enqueue("Shalom")
tempatKasir.printAll()

tempatKasir.dequeue()
tempatKasir.printAll()

