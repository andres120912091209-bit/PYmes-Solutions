package com.pymessolutions.pymes_solutions.service;

import com.pymessolutions.pymes_solutions.model.Client;
import com.pymessolutions.pymes_solutions.repository.ClientRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ClientService {

    private final ClientRepository clientRepository;

    public ClientService(ClientRepository clientRepository) {
        this.clientRepository = clientRepository;
    }

    public List<Client> findAll() {
        return clientRepository.findAll();
    }

    public Client findById(Long id) {
        return clientRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Cliente no encontrado con id: " + id));
    }

    public Client save(Client client) {
        if (clientRepository.existsByEmail(client.getEmail())) {
            throw new RuntimeException("El email ya está registrado");
        }
        return clientRepository.save(client);
    }

    public Client update(Long id, Client clientDetails) {
        Client client = findById(id);
        client.setName(clientDetails.getName());
        client.setEmail(clientDetails.getEmail());
        client.setPhone(clientDetails.getPhone());
        client.setCompany(clientDetails.getCompany());
        client.setIsActive(clientDetails.getIsActive());
        return clientRepository.save(client);
    }

    public void delete(Long id) {
        Client client = findById(id);
        clientRepository.delete(client);
    }
}