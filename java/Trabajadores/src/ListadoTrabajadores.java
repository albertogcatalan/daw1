
public class ListadoTrabajadores {

	/**
	 * @param args
	 */
	
	// metodo que recorre el array de los trabajadores
	public static void pagar (Trabajador trabajadores[])
	{
		int i;
	    for (i=0; i<trabajadores.length; i++)
	        realizarTransferencia ( trabajadores[i]);
	} 
	
	// metodo que recorre el array de los trabajadores alfabeticamente
	public static void pagarOrdenadoAlfabetico (Trabajador[] trabajadores)
	{
		Trabajador temp = null;
		int n = trabajadores.length;
	    for (int pass=1; pass < n; pass++) {  // count how many times
	        // This next loop becomes shorter and shorter
	        for (int i=0; i < n-pass; i++) {
	            if (trabajadores[i].getNombre().compareTo(trabajadores[i+1].getNombre()) > 0) {
	                // exchange elements
	                temp = trabajadores[i];  trabajadores[i] = trabajadores[i+1];  trabajadores[i+1] = temp;
	        
	            }
	        }
	    }
	    
	    for (int i=0; i<trabajadores.length;i++){
	    	System.out.println(trabajadores[i]);
	    }
	    
	} 
	
	    
	private static void realizarTransferencia(Trabajador trabajador) {
		// metodo que muestra por pantalla la informacion de los trabajadores
		System.out.println("---------------------------------");
		System.out.println(trabajador + " " + trabajador.calcularPaga() + "Û");
		
	}


	public static void main(String[] args) {
		// 10 trabajadores (6 empleados y 4 consultores)
		Trabajador trabajadores[] = new Trabajador[10];
		
		//empleados
		trabajadores[0] = new Empleado
		                   ("Jose", "123", 24000.0);
		trabajadores[1] = new Empleado
                 ("Pepe", "321", 21000.0);
		trabajadores[2] = new Empleado
                 ("Alberto", "762", 25000.0);
		trabajadores[3] = new Empleado
                 ("Luis", "245", 8000.0);
		trabajadores[4] = new Empleado
                 ("Sorin", "789", 24080.0);
		trabajadores[5] = new Empleado
                 ("Jose", "456", 54000.0);
		
		//consultores
		trabajadores[6] = new Consultor
		                   ("Juan", "456", 11, 40.0);
		trabajadores[7] = new Consultor
                 ("Pedro", "908", 10, 56.0);
		trabajadores[8] = new Consultor
                 ("Joaquin", "875", 20, 32.0);
		trabajadores[9] = new Consultor
                 ("Andrea", "299", 40, 90.0);
		
		//recorrer array y pintar por pantalla
		pagar(trabajadores);
		
		System.out.println("---------------------------------");
		
		System.out.println("\n**Ordenado por Nombre Alfabeticamnte**");

		pagarOrdenadoAlfabetico(trabajadores);
		
		System.out.println("****************");

		
	}

}
