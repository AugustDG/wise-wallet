package com.controller;

import com.model.Item;
import com.service.ItemService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.xml.ws.Response;
import java.util.List;

@RestController
@RequestMapping("/item")
public class ItemController {

    @Autowired
    private ItemService itemService;

    @PostMapping("/checkPrices")
    public ResponseEntity<List<Item>> checkPrices(@RequestBody List<Item> itemList) {

        itemList = itemService.getBetterPrices(itemList);

        return new ResponseEntity<>(itemList, HttpStatus.OK);
    }
}
