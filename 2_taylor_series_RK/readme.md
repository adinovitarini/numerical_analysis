# Deret Taylor
Metode Taylor untuk menyelesaikan persamaan diferensial $\frac{dy}{dt}=f(t,y)$, maka dapat diselesaikan sebagai berikut 
### Ekspansi deret Taylor 
$$y(t+h) = y(t)+h\underbrace{\frac{dy}{dt}}\_{f(t,y)}+\underbrace{h^2\frac{d^2y}{dt^2}}\_{O(h^2)}+\underbrace{h^3\frac{d^3y}{dt^3}}\_{O(h^3)}+\dots$$
Jika elemen $O(h^2)$ dan orde di atasnya **dihilangkan**, maka ekspansi derte Taylor dapat dinyatakan sbb: 
$$y(t+h)=y(t)+hf(t,y)$$
Persamaan di atas dikenal sebagai Metode Euler. 
Jika elemen $O(h^2)$ dan orde di atasnya **tidak dihilangkan**, maka kita perlu menghitung turunan pertama, kedua, dan seterusnya. Perlu diingat aturan _chain rule_ untuk persamaan diferensial parsial, yakni:
$$\frac{du}{dt}=\frac{\partial u}{\partial x}\frac{dx}{dt}$$
# Metode Runge-Kutta orde 2 
$f(t_i,y_i)$ =  
## Hasil Simulasi 
Contoh soal: $\frac{dy}{dt} = y - t^2 + 1$ dengan $y(0) = 0.5$
![image](https://github.com/user-attachments/assets/e6f75967-e606-40a9-8fd6-34cc59016456)
