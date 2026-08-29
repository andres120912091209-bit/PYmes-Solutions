package com.pymessolutions.pymes_solutions.repository;

import com.pymessolutions.pymes_solutions.model.Product;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ProductRepository extends JpaRepository<Product, Long> {
}