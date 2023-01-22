package bruh.repository;

import bruh.model.Item;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ItemRepository extends JpaRepository<Item, Integer> {
    @Query(value = "SELECT * FROM fruits", nativeQuery = true)
    public List<Item> getItemList();
}