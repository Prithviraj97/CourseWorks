//Name: Prithvi Raj Singh
//Date: 10/5/20
//Purpose: Responsible for creating a node containing a town that is linked to a parent node.

import java.text.*;

public class SearchNode 
{
    private Town town;
    private double pathCost;
    private SearchNode parent;
    
    public SearchNode(Town tow, SearchNode par, double cos)
            {
                town = tow;
                parent = par;
                pathCost= cos;
            }
    
    public String toString()
    {
        DecimalFormat decFor= new DecimalFormat("####.00");
        String solution= ""+town.getName()+":"+decFor.format(pathCost)+", ";
        SearchNode sNode= parent;
        
        while(sNode!=null)
        {
            solution= sNode.getTown().getName()+decFor.format(sNode.getPathCost())+" "+solution;
            sNode= sNode.getParent();
        }
        return solution;
    }

   
    public Town getTown() 
    {
        return town;
    }

   
    public double getPathCost() 
    {
        return pathCost;
    }

    public SearchNode getParent() 
    {
        return parent;
    }
    
}
