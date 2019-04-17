import java.util.ArrayList;

public class Club
{
   ArrayList<Membership> memberships;
    
    /**
     * Constructor for objects of class Club
     */
    public Club()
    {
        memberships = new ArrayList<>();
        
    }

    /**
     * Add a new member to the club's list of members.
     * @param member The member object to be added.
     */
    public void join(Membership member)
    {
        System.out.println("Antes tinhamos " + this.numberOfMembers() + " membros");
        this.memberships.add(member);
        System.out.println("Agora temos " + this.numberOfMembers() + " membros");
    }

    /**
     * @return The number of members (Membership objects) in
     *         the club.
     */
    public int numberOfMembers()
    {
        return this.memberships.size();
    }
}
