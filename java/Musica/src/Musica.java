
public class Musica {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Album mialbum;
		
		mialbum = new Album("Wrecking Ball");
		
		System.out.println(mialbum);
		
		mialbum.carga_canciones("Wrecking_Ball.csv");
		
		System.out.println(mialbum);
		
		
	}

}
