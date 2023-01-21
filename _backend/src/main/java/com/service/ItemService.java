package com.service;

import com.model.Item;
import lombok.NoArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@NoArgsConstructor
public class ItemService {


    public List<Item> getBetterPrices(List<Item> itemList) {

        

        for (Item item: itemList) {

        }

        return itemList;
    }
}
