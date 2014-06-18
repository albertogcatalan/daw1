
public class AutoresLibros {

	/**
	 * Probando las clases autor y libro
	 */
	public static void main(String[] args) {
		// inicializamos el objeto libro y autor con 5 espacios en el vector
		Autor autores[] = new Autor[5];
		Libro libros[] = new Libro [5];
		
		//insertamos 5 autores
		autores[0] = new Autor("autor1", "email1", 'm');
		autores[1] = new Autor("autor2", "email2", 'm');
		autores[2] = new Autor("autor3", "email3", 'f');
		autores[3] = new Autor("autor4", "email4", 'm');
		autores[4] = new Autor("autor5", "email5", 'f');
		
		//insertamos 5 libros con los anteriores autores
		libros[0] = new Libro("libro1", autores[0], 100, 1);
		libros[1] = new Libro("libro2", autores[1], 555, 2);
		libros[2] = new Libro("libro3", autores[2], 100, 5);
		libros[3] = new Libro("libro4", autores[3], 5, 3);
		libros[4] = new Libro("libro5", autores[4], 8976, 5);
		
		//recorremos los libros mostrando su información
		for (int i=0; i<libros.length;i++){
			System.out.println(libros[i].toString());
		}
		
		
	}

}
