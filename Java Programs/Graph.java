//Name:Prithvi Raj Singh
//Date: 10/5/20
//Purpose: Graph is the main class. Responsible for creating a hashmap of towns,
//reading in towns from file and loading in roads from file.
//contains the search algorithm for BFS and DFS.

import java.util.*;
import java.io.*;

public class Graph {
    
    private HashMap<String, Town> map;
    private String name;
    
    public Graph(String nam, String cityFname, String edgeFname)
    {
        name = nam;
        map = new HashMap<String, Town>();
        loadTownsFromFile(cityFname);
        loadRoadsFromFile(edgeFname);
    }
    public String getSolutionFromBFS(String initialname, String goalname)
    {
        if(map.get(initialname)==null)
        {
            return "\nThe Town "+ initialname+" doesn't exist";
        }
        if(map.get(goalname)==null)
        {
            return "\nThe Town "+ goalname+" doesn't exist";
        }
        Town initialNode= map.get(initialname);
        Town goal = map.get(goalname);
        SearchNode startNode= BFS(initialNode, goal);
        return startNode.toString();
    }
    public SearchNode BFS(Town startNode, Town goal)
    {
        SearchNode rootNode = new SearchNode(startNode, null, 0);
        if(rootNode.getTown().getName().equals(goal.getName()))
        {
            return rootNode;
        }
        LinkedList<SearchNode> frontier = new LinkedList<>();
        frontier.add(rootNode);
        
        LinkedList<Town> explored = new LinkedList<>();
        
        while(true)
        {
            if(frontier.isEmpty())
                return null;
            
            SearchNode currentSN = frontier.get(0);
            frontier.remove(0);
            
            Town curTown= currentSN.getTown();
            if(curTown.getName().equals(goal.getName()))
                return currentSN;
            explored.add(curTown);
            
            int childCount =  curTown.countRoads();
            for(int chi=0; chi<childCount; chi++)
            {
                Town child= curTown.getRoad(chi).getTown();
                if(explored.contains(child))
                    continue;
                if(checkFrontier(frontier, child))
                    continue;
                SearchNode newSN= new SearchNode(child, currentSN, 
                        currentSN.getPathCost()+curTown.getRoad(chi).getDistance());
                frontier.add(newSN);
                
            }
            purgeFrontier(frontier, curTown);
        }
    }
    
    public String getSolutionFromDFS(String initialname, String goalname)
    {
        Town initialNode= map.get(initialname);
        Town goal = map.get(goalname);
        SearchNode startNode= BFS(initialNode, goal);
        return startNode.toString();
    }
    public SearchNode DFS(Town startNode, Town goal)
    {
        SearchNode rootNode = new SearchNode(startNode, null, 0);
        if(rootNode.getTown().getName().equals(goal.getName()))
        {
            return rootNode;
        }
        LinkedList<SearchNode> frontier = new LinkedList<>();
        frontier.add(rootNode);
        
        LinkedList<Town> explored = new LinkedList<>();
        
        while(true)
        {
            if(frontier.isEmpty())
                return null;
            
            SearchNode currentSN = frontier.get(0);
            frontier.remove(0);
            
            Town curTown= currentSN.getTown();
            if(curTown.getName().equals(goal.getName()))
                return currentSN;
            explored.add(curTown);
            
            int childCount =  curTown.countRoads();
            for(int chi=0; chi<childCount; chi++)
            {
                Town child= curTown.getRoad(chi).getTown();
                if(explored.contains(child))
                    continue;
                if(checkFrontier(frontier, child))
                    continue;
                SearchNode newSN= new SearchNode(child, currentSN, 
                        currentSN.getPathCost()+curTown.getRoad(chi).getDistance());
                frontier.addFirst(newSN);
                
            }
            purgeFrontier(frontier, curTown);
        }
    }

    
    public boolean checkFrontier(LinkedList<SearchNode>front, Town tow)
    {
        int size= front.size();
        for(int dex= 0; dex<size; dex++)
        {
            if(front.get(dex).getTown()== tow)
                return true;
        }
        return false;
    }
    
    public boolean purgeFrontier(LinkedList<SearchNode>front, Town tow)
    {
        boolean flag= false;
        int size= front.size();
        for(int dex= 0; dex<size; dex++)
        {
            if(front.get(dex).getTown()== tow)
            {
                front.remove(dex);
                dex--;
                size--;
                flag= true;
            }
        }
        return flag;
    }
    
    public void loadTownsFromFile(String fname)
    {
        try
        {
            Scanner inScan = new Scanner(new File (fname)).useDelimiter("[,\n]");
            while(inScan.hasNext())
            {
                String nam= inScan.next();
                //System.out.println(nam);
                
                int pop = inScan.nextInt();
                //System.out.println(pop);
                
                int date= inScan.nextInt();  
                //System.out.println(date);
                
                Town curTown = new Town(nam,pop,date);
                map.put(nam, curTown);                
            }
        }
        catch(IOException ioe)
        {
            System.out.print("\nA IOException was thrown yyyyyyyyyyyyyy\n");
        }
    }
    
    public void loadRoadsFromFile(String fname)
    {
       try
       {
           Scanner inScan= new Scanner(new File (fname)).useDelimiter("[,\n]");
           while(inScan.hasNext())
           {
               String Town1= inScan.next();
               String Town2 = inScan.next();
               double distance = inScan.nextDouble();
               if((map.get(Town1)== null)|| (map.get(Town2)==null))
                   continue;
               map.get(Town1).addRoad(distance, map.get(Town2));
               map.get(Town2).addRoad(distance, map.get(Town1));
           }
       }
       catch(IOException ioe)
       {
           System.out.print("\n Error in loading roads from file");
       }
       System.out.print("\n\n"+toString()+"\n\n");
    }
    
    public String toString()
    {
        Set<String> allTown = map.keySet();
        Iterator townIter = allTown.iterator();
        String stuff = "\n"+ name+"\n";
        while(townIter.hasNext())
        {
            String key=(String)townIter.next();
            Town curTown = map.get(key);
            stuff+="\n"+curTown.toString();
        }
        return stuff+"\n";
    }
    
    public Town getTown(String name)
    {
        return map.get(name);
    }
    

    
    public static void main(String[] args) {
        // TODO code application logic here
        Graph myGraph= new Graph("Small map","citie_2.txt", "edges_2.txt");
        System.out.print("\nBFS ----> "+myGraph.getSolutionFromBFS("Telluro", "Telluro"));
        System.out.print("\nDFS ----> "+myGraph.getSolutionFromDFS("Telluro", "Telluro"));
        
    }
    
}
