public class Libro {
	
	private String name;
	private Autor autor;
	private double price;
	private int qtyInStock;
	
	public Libro(String name, Autor autor, double price, int qtyInStock) {
		
		this.name = name;
		this.autor = autor;
		this.price = price;
		this.qtyInStock = qtyInStock;
	
	}

	public double getPrice() {
		return price;
	}


	public void setPrice(double price) {
		this.price = price;
	}


	public int getQtyInStock() {
		return qtyInStock;
	}


	public void setQtyInStock(int qtyInStock) {
		this.qtyInStock = qtyInStock;
	}


	public String getName() {
		return name;
	}

	public Autor getAutor() {
		return autor;
	}

	public String getAuthorName(){
		return autor.getName();
	}
	
	public String getAuthorEmail(){
		return autor.getEmail();
	}
	
	public char getAuthorGender(){
		return autor.getGender();
	}
	
	public String toString() {
		return name + " escrito por " + "("+autor+")";
	}
		
}