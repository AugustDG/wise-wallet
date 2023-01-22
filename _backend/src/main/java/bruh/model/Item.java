package bruh.model;


import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name="fruits")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@ToString
public class Item {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    private String fruit;

    private float curPrice;

    private float bestPrice;

    private String bestPriceUrl;



}
