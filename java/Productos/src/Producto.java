public class Producto extends Precio {
  // Atributos
  public int codigo;
  
  //constructor
  
  public Producto(int cod, double p){
	  setCodigo(cod);
	  setEuros(p);
  }
  
 public Producto(){
	 
 }
  
  // Metodos
  public int getCodigo() {
		return codigo;
	}
	public void setCodigo(int codigo) {
		this.codigo = codigo;
	}  

  public void asignaProducto(int cod,
                           double p) {
    setCodigo(cod); 
    setEuros(p);
  }
  
  public String toString() {
    return "Codigo: " + codigo +
           " ; Precio: " + euros +
           "Û"; }

 
  }
