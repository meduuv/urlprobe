# URLProbe

> Normalize URLs and perform simple endpoint reachability diagnostics.

URLProbe is a lightweight utility for normalizing HTTP and HTTPS endpoints and checking basic reachability information.

## Highlights

- URL normalization
- HTTP and HTTPS endpoint diagnostics
- Useful request metadata for troubleshooting
- Simple output suitable for scripts
- Focused on diagnostics rather than exploitation

## Usage

```bash
urlprobe https://example.com
urlprobe https://example.com --json
```

## Workflow

```text
URL
 ↓
normalize
 ↓
endpoint check
 ↓
structured diagnostics
```

## Use Cases

- API troubleshooting
- Endpoint health checks
- Development diagnostics
- Automation workflows
- Web tooling experiments

Use URLProbe only against endpoints you own or are permitted to assess.

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
