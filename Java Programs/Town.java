//Name: Prithvi Raj Singh
//Date: 10/5/20
//Purpose: Responsible for a creating Town with name, date, population and roads from the town.

import java.util.*;
public class Town {
    
    private String name;
    private int population;
    private int date;
    private LinkedList roads;
    
    public Town(String nam, int pop, int dat){
        date = dat;
        name = nam;
        population = pop;
        roads = new LinkedList();
    }
    
    public void addRoad(double dis, Town tow){
        roads.add(new Route(dis,  tow));
    }
    
    public double getPopulation(){
        return population;
    }
    
    public int countRoads(){
        return roads.size();
    }
    
    public Route getRoad(int dex){
        return (Route) roads.get(dex);
    }
    
    public int getDate(){
        return date;
    }
    
    public String getName(){
        return name;
    }
    
    public String toString(){
        String stuff = name+", population: " +population+", founded in "+date+ "\n\troads---->";
        
        if(roads.size() > 0){
            int dex = 0;
            while(dex < roads.size()){
                Route curRoute = (Route) roads.get(dex);
                stuff += curRoute.toString();
                dex++;
            }
        }
        return stuff;
    }
}
