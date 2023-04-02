//Name:Prithvi Raj Singh
//Date: 10/5/20
//Purpose: Responsible for creating links between towns with the distance.

public class Route {
    
    private double distance;
    private Town town;
    
    public Route(double dis, Town t){
        distance = dis;
        town = t;
    }
    
     public String toString(){
         return " "+distance+" to "+town.getName()+", ";
     }
     
     public double getDistance(){
         return distance;
     }
     
     public Town getTown(){
         return town;
     }
}
