package com.pymessolutions.pymes_solutions.repository;

import com.pymessolutions.pymes_solutions.model.user;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface userRepository extends JpaRepository<user, Long> {
    Optional<user> findByEmail(String email);
    boolean existsByEmail(String email);
}