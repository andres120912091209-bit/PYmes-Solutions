package com.pymessolutions.pymes_solutions.service;

import com.pymessolutions.pymes_solutions.model.user;
import com.pymessolutions.pymes_solutions.repository.userRepository;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.Map;

@Service
public class AuthService {

    private final userRepository userRepository;

    public AuthService(userRepository userRepository) {
        this.userRepository = userRepository;
    }

    public user register(user user) {
        if (user.getName() == null || user.getName().isBlank()) {
            throw new RuntimeException("El nombre es obligatorio");
        }
        if (user.getEmail() == null || user.getEmail().isBlank()) {
            throw new RuntimeException("El email es obligatorio");
        }
        if (user.getPassword() == null || user.getPassword().isBlank()) {
            throw new RuntimeException("La contraseña es obligatoria");
        }
        if (userRepository.existsByEmail(user.getEmail())) {
            throw new RuntimeException("El email ya está registrado");
        }
        return userRepository.save(user);
    }

    public Map<String, Object> login(String email, String password) {
        user user = userRepository.findByEmail(email)
                .orElseThrow(() -> new RuntimeException("Credenciales incorrectas"));

        if (!user.getPassword().equals(password)) {
            throw new RuntimeException("Credenciales incorrectas");
        }

        Map<String, Object> response = new HashMap<>();
        response.put("message", "Inicio de sesión exitoso");
        response.put("userId", user.getId());
        response.put("name", user.getName());
        response.put("email", user.getEmail());
        return response;
    }
}