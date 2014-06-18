import java.sql.*;

public class ConexionSqlite {

	/**
	 * @param args
	 * @throws ClassNotFoundException 
	 * @throws SQLException 
	 */
	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		// cargar el driver
		Class.forName("org.sqlite.JDBC");
		
		// conectar con la base de datos
		String cadena_con = "jdbc:sqlite:ejemplo.db";
		Connection conn = DriverManager.getConnection(cadena_con);
		
		// acceder a la base de datos
		Statement sentencia = conn.createStatement();
		sentencia.executeUpdate("create table people (name, occupation);");
		 PreparedStatement prep = conn.prepareStatement(
			      "insert into people values (?, ?);");

			    prep.setString(1, "Gandhi");
			    prep.setString(2, "politics");
			    prep.addBatch();
			    prep.setString(1, "Turing");
			    prep.setString(2, "computers");
			    prep.addBatch();
			    prep.setString(1, "Wittgenstein");
			    prep.setString(2, "smartypants");
			    prep.addBatch();
			    prep.setString(1, "Alberto");
			    prep.setString(2, "masterfucker");
			    prep.addBatch();
			    
		// procesar el resultado
		String consulta = "select * from people;";
		
		ResultSet rs = sentencia.executeQuery(consulta);
		
		while (rs.next()){
			System.out.println("Nombre: "+ rs.getString("name"));
			System.out.println("Nombre: "+ rs.getString("occupation"));
			
		}
		
		// cierre de la conexi—n
		rs.close();
	    conn.close();

	}

}
