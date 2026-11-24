# atlas-foundry-144

Current version: `1.0.0`.

> Work in progress. This checkpoint may be incomplete or fail tests. See PLAN.md and STATUS.md before use.


Free AI/ML model access - DeepSeek V4.1 Flash, Kimi K3 and other frontier models.

## Installation

```bash
# Install as dsh plugin
dsh plugin install atlas-foundry-144

# Or via npm
npm install atlas-foundry-144
```

## Usage

No login, no sign-up, no API key required. The frontier models are just there.

```bash
# List available models
atlas-foundry-144 models

# Access DeepSeek V4.1 Flash
atlas-foundry-144 chat --model deepseek-v4.1-flash

# Access Kimi K3
atlas-foundry-144 chat --model kimi-k3
```

## Available Models

| Model | Provider | Description |
|-------|----------|-------------|
| `deepseek-v4.1-flash` | DeepSeek | Free tier with no usage cap |
| `kimi-k3` | Kimi | Free tier with no usage cap |
| `glm-5.3-flash` | Z.ai | Free tier inference |

## License

MIT License - Copyright (c) 2026 Alan Vo

See [LICENSE](LICENSE) for full terms.

## Contact

- [alanvo.net](https://alanvo.net)
- [@alanvoasi on X](https://x.com/alanvoasi)

## References

- dsh-our-free-model: [GitHub](https://github.com/Ebony-Vinyl/dsh-our-free-model)
- Issue #845: Full free usage restrictions
- Issue #868: AGPL §13 source code provision

Maintainer: Alan Vo <alanvo@gmail.com>
