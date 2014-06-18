import java.sql.*;

public class ConexionMysql {

	/**
	 * @param args
	 * @throws ClassNotFoundException 
	 * @throws SQLException 
	 */
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// cargar el driver
		Class.forName("com.mysql.jdbc.Driver");
		
		// conectar con la base de datos
		String cadena_con = "jdbc:mysql:thin:@172.30.167.8:1521:xe";
		Connection conn = DriverManager.getConnection(cadena_con, "hr", "case");
		System.out.println("Terminado");
	
		

	}

}
