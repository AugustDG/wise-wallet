package bruh.service;

import bruh.model.Item;
import bruh.repository.ItemRepository;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
@NoArgsConstructor
public class ItemService {

    @Autowired
    private ItemRepository itemRepository;

    public List<Item> getBetterPrices(List<Item> itemList) {

        List<Item> itemListFromDb = itemRepository.getItemList();
        Map<String, Item> itemMap = new HashMap<>();

        for (Item i: itemListFromDb) {
            itemMap.put(i.getFruit(), i);
        }

        List<Item> itemListWithBetterPrice = new ArrayList<>();


        for (Item item: itemList) {

            if (itemMap.containsKey(item.getFruit()) && (item.getCurPrice() > itemMap.get(item.getFruit()).getBestPrice())) {
                Item temp = itemMap.get(item.getFruit());
                temp.setCurPrice(item.getCurPrice());
                itemListWithBetterPrice.add(temp);
            }
        }

        return itemListWithBetterPrice;
    }
}
