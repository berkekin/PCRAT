# pythonransomware

EN:   
In simple terms, the code does the following:Encryption Key Generation: The code generates a random key (encryption key) for the AES encryption algorithm.

Finding and Encrypting Files:

It finds all files located on the computer's system drive (usually the C: drive).
It encrypts each file using the AES algorithm.
It creates a new file for each encrypted file and adds .encrypted to the name of the original file. For example, the file example.txt is encrypted as example.txt.encrypted.
Deletes the original files.
Exclude Windows Directory: The code performs encryption by excluding the directory containing Windows' system files. This ensures that the operating system continues to work.

Notifying the User: When the process is completed, a message box informs the user that all files have been encrypted and their original state has been deleted.

Detailed explanation for developers: Importing Libraries: The code uses the Crypto.Cipher and Crypto.Random modules for encryption operations, the os module for file operations, and the tkinter library to provide information to the user.

Padding Function (pad) for Encryption Process:

AES encryption requires a certain block size of data. If the data does not fit this size completely, the pad function makes the data suitable by filling the missing part with zeros (\0).
File Encryption Function (encrypt_file):

It opens the file via the given file path and reads its content.
Generates a random starting vector (iv). This ensures that the encryption is different each time.
It encrypts data with the AES encryption algorithm.
Writes the encrypted data to a new file along with the starting vector. Thus, the data required for decryption is also recorded.
Deletes the original file from the system.
Main Function of Ransomware (ransomware):

It scans all files on the computer's main drive (system_drive).
Windows calls the encrypt_file function for each file found, except for the directory containing system files.
This process encrypts almost all user files on the system drive.
Main Program (if __name__ == '__main__'):

When the program is run, it generates a 256-bit encryption key and calls the ransomware function with this key.
In case of any error, it displays the error message to the user through a window.
What this code does is designed to restrict user access and potentially demand a ransom to get the files back.



TR: TR:
Basit bir ifadeyle kod şunları yapar: Şifreleme Anahtarı Oluşturma: Kod, AES şifreleme algoritması için rastgele bir anahtar (şifreleme anahtarı) oluşturur.

Dosyaları Bulma ve Şifreleme:

Bilgisayarın sistem sürücüsünde (genellikle C: sürücüsü) bulunan tüm dosyaları bulur.
Her dosyayı AES algoritmasını kullanarak şifreler.
Her şifrelenmiş dosya için yeni bir dosya oluşturur ve orijinal dosyanın adına .encrypted ifadesini ekler. Örneğin, example.txt dosyası example.txt.encrypted olarak şifrelenir.
Orijinal dosyaları siler.
Windows Dizinini Hariç Tut: Kod, Windows'un sistem dosyalarını içeren dizini hariç tutarak şifrelemeyi gerçekleştirir. Bu, işletim sisteminin çalışmaya devam etmesini sağlar.

Kullanıcının Bilgilendirilmesi: İşlem tamamlandığında, bir mesaj kutusu kullanıcıya tüm dosyaların şifrelendiği ve orijinal durumlarının silindiği konusunda bilgi verir.

Geliştiriciler için detaylı açıklama: Kütüphaneleri İçe Aktarma: Kod, şifreleme işlemleri için Crypto.Cipher ve Crypto.Random modüllerini, dosya işlemleri için os modülünü ve kullanıcıya bilgi sağlamak için tkinter kütüphanesini kullanır.

Şifreleme İşlemi için Dolgu Fonksiyonu (pad):

AES şifrelemesi belirli bir blok boyutunda veri gerektirir. Eğer veri bu boyuta tam olarak uymuyorsa pad fonksiyonu eksik kısmı sıfırlarla (\0) doldurarak veriyi uygun hale getirir.
Dosya Şifreleme İşlevi (encrypt_file):

Dosyayı verilen dosya yolu üzerinden açar ve içeriğini okur.
Rastgele bir başlangıç ​​vektörü (iv) oluşturur. Bu, şifrelemenin her seferinde farklı olmasını sağlar.
Verileri AES şifreleme algoritmasıyla şifreler.
Şifrelenmiş verileri başlangıç ​​vektörüyle birlikte yeni bir dosyaya yazar. Böylece şifrenin çözülmesi için gerekli olan veriler de kayıt altına alınmış olur.
Orijinal dosyayı sistemden siler.
Fidye Yazılımının (fidye yazılımı) Ana İşlevi:

Bilgisayarın ana sürücüsündeki (system_drive) tüm dosyaları tarar.
Windows, sistem dosyalarını içeren dizin dışında bulunan her dosya için encrypt_file işlevini çağırır.
Bu işlem, sistem sürücüsündeki hemen hemen tüm kullanıcı dosyalarını şifreler.
Ana Program (eğer __name__ == '__main__' ise):

Program çalıştırıldığında 256 bitlik bir şifreleme anahtarı oluşturur ve bu anahtarla fidye yazılımı fonksiyonunu çağırır.
Herhangi bir hata durumunda kullanıcıya hata mesajını bir pencere aracılığıyla gösterir.
Bu kodun yaptığı şey, kullanıcı erişimini kısıtlamak ve potansiyel olarak dosyaları geri almak için fidye talep etmek için tasarlanmıştır.
