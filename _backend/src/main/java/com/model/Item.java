package com.model;


import jakarta.persistence.*;

@Entity
@Table(name="fruitsandvegetables")
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;


}
