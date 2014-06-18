/*
Construir una clase Racional con:
Atributos
numerador: de tipo double
denominador: de tipo double
M√©todos:
public void asignar(double x, double y){}
public void asignaNumerador(int x){}
Public void asignaDenominador(int y){}
public void imprimir(){}
public String toString(){}
public void Simplificar(){}
public void sumar(Racional b){}
public void sumar(Racional a, Racional b){}
public void producto(Racional a, Racional b){}
Construir una clase PruebaRacional que contenga un m√©todo principal que trabaje con instancias de la clase Racional.
*/
public class Racional {
    
    public int numerador;
    public int denominador;
    
    public void asignar(int x, int y){
    	numerador = x;
    	denominador = y;
    }
    public String toString(){
    	return numerador + " / " + denominador;
    }
    private void simplificar(){
    	int divisor = gcd(numerador, denominador);
    	numerador = numerador / divisor;
    	denominador = denominador / divisor;
    	
    }
    public void sumar(Racional r){
    	int nuevoNumerador = 0;
    	int nuevoDenominador = 0;
    	nuevoNumerador = numerador * r.denominador + 
    			denominador * r.numerador;
    	
    	nuevoDenominador = denominador * r.denominador;
    	numerador = nuevoNumerador;
    	denominador = nuevoDenominador;
    	simplificar();
    }
    // método que devuelve el máximo comun divisor
    private static int gcd(int a, int b){
    	if (b == 0){
    		return a;
    	}
    	int r = a % b;
    	return gcd(b, r);
    }
    public void producto(Racional a, Racional b){
    	return;
    	
    }
    
}