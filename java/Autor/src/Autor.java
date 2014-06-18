
public class Autor {
	
	public String name;
	public String email;
	public char gender;
	
	

	public String getEmail() {
		return email;
	}


	public void setEmail(String email) {
		this.email = email;
	}


	public String getName() {
		return name;
	}


	public char getGender() {
		return gender;
	}

	
	public Autor(String name, String email, char gender) {
		
		this.name = name;
		this.email = email;
		this.gender = gender;
	}


	public String toString(){
		return name+"("+email+")";
	}

}
