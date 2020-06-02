package tw.b2e.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @Value("${custom.key}")
    private String key;

    @GetMapping("/env")
    public String test() {
        String first = System.getenv("first");
        String last = System.getenv("last");
        return String.format("key=%s, first=%s, last=%s", key, first, last);
    }

}
