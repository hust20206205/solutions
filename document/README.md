tối nay phair xong ddd 
nếu có thể thì làm cái nghiệp vụ
<!--  -->
<!-- Hãy sử dụng Ngôn ngữ chung (Ubiquitous Language) trong domain driven design (DDD) với nội dung nghiệp vụ kinh doanh sau: -->

<!-- 1. **Khách hàng (Customer):** -->
<!-- - **Mô tả:** Người sử dụng dịch vụ, có thể là cá nhân hoặc tổ chức. -->

<!-- 2. **Hóa đơn điện tử (Electronic Invoice):** -->
<!-- - **Mô tả:** Hóa đơn được tạo và quản lý điện tử thay vì truyền thống trên giấy. -->

<!-- Bằng cách sử dụng ngôn ngữ chung như trên, chúng ta có thể tạo ra một mô hình DDD rõ ràng và dễ hiểu, giúp các đội phát triển, quản lý dự án và người dùng hiểu rõ về các yêu cầu và chức năng của hệ thống. -->
<!--@ -->
<!--@ -->

<!--@ -->
<!--@ -->

https://viblo.asia/p/domain-driven-design-phan-2-MgNeWoZAeYx

https://culttt.com/search
https://culttt.com/2014/04/09/use-exception
https://culttt.com/2014/08/18/encapsulating-applications-business-rules
https://culttt.com/2014/09/29/creating-domain-services
https://culttt.com/2014/12/08/creating-domain-objects-recap
https://culttt.com/2014/12/17/aggregates-domain-driven-design
https://culttt.com/2014/12/24/factories-domain-driven-design
https://culttt.com/2014/12/29/enforcing-business-rules-aggregate-instantiation
https://culttt.com/2014/04/30/difference-entities-value-objects
https://culttt.com/2015/01/05/using-aggregates-gateway-functionality
https://culttt.com/2015/01/07/service-oriented-architecture
https://culttt.com/2015/01/14/command-query-responsibility-segregation-cqrs
https://culttt.com/2015/11/11/what-is-active-model

<!--@ -->
<!--@ -->
<!--@ -->
<!--@ -->
<!--@ -->
<!--@ -->

Trình bày về Các mẫu chiến lược (Strategic Patterns) trong domain driven design
https://ddd-practitioners.com/home/glossary
<!--@ -->
<!--@ -->
<!--@ -->

<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->
<!--@Các khuôn mẫu trong thiết kế hướng miền-->

<!-- Domain Object : https://ddd-practitioners.com/domain-object -->
<!-- Entity : https://ddd-practitioners.com/entity -->
<!-- [[Entity]] An object fundamentally defined not by its attributes, but by a thread of continuity and identity. -->
<!-- Entity Identity : https://ddd-practitioners.com/entity-identity -->
<!-- Value Object : https://ddd-practitioners.com/home/glossary/value-object -->
<!-- [[Value Object]] An object that describes some characteristic or attribute but carries no concept of identity. -->
<!-- Service : https://ddd-practitioners.com/service -->
<!-- [[Service]] An operation offered as an interface that stands alone in the model, with no encapsulated state. -->

<!-- Quản lí vòng đời -->
<!-- [[Life Cycle]] A sequence of states an object can take on between creation and deletion, typically with constraints to ensure integrity when changing from one state to another. May include migration of an [[Entity]] between systems and different [[Bounded Contexts]]. -->
<!-- Aggregate: https://ddd-practitioners.com/home/glossary/aggregate/ -->
<!-- [[Aggregate]] A cluster of associated objects that are treated as a unit for the purpose of data changes. External references are restricted to one member of the AGGREGATE, designated as the root. A set of consistency rules applies within the AGGREGATE’S boundaries. -->
<!-- State Stored Aggregates : https://ddd-practitioners.com/state-stored-aggregate -->
<!-- Consistency Boundary : https://ddd-practitioners.com/glossary/consistency-boundary -->
<!-- Factory : https://ddd-practitioners.com/factory -->
<!-- [[Factory]] A mechanism for encapsulating complex creation logic and abstracting the type of a created object for the sake of a client. -->

https://refactoring.guru/design-patterns/factory-method
https://refactoring.guru/design-patterns/abstract-factory
https://culttt.com/2014/12/24/factories-domain-driven-design

<!-- Repository : https://ddd-practitioners.com/?page_id=555 -->
<!-- [[Repository]] A mechanism for encapsulating storage, retrieval, and search behavior which emulates a collection of objects. -->
<!-- Module : https://ddd-practitioners.com/?page_id=618 -->

<!-- CI/CD -->

<!-- Bounded Context: https://ddd-practitioners.com/home/glossary/bounded-context -->
[[Context]] The setting in which a word or statement appears that determines its meaning. See [[Bounded Context]].

Mỗi bounded context nên tương ứng với một nhóm hoặc bộ phận cụ thể trong tổ chức. Sự tương ứng này có thể giúp giảm thiểu sự hiểu lầm và tăng khả năng tương tác giữa các đội ngũ.

Ví dụ: khách hàng có thể có nhiều ý nghĩa khác nhau tùy thuộc vào ngữ cảnh: trong ngữ cảnh thanh toán, đó là người nợ tiền; trong bối cảnh vận chuyển, đó là người nhận hàng. Bằng cách tạo một mô hình riêng cho từng ngữ cảnh, bạn có thể tránh nhầm lẫn và làm cho mã rõ ràng hơn.

<!-- Bounded Context Relationships : https://ddd-practitioners.com/bounded-context-relationship -->

<!-- Context Mapping : https://ddd-practitioners.com/context-map -->
[[Context Map]] A representation of the [[Bounded Context]]s involved in a project and the actual relationships between them and their models.

Hữu ích cho việc hiểu kiến ​​trúc tổng thể

<!-- Separate Ways : https://ddd-practitioners.com/separate-ways -->
<!-- Customer/Supplier : https://ddd-practitioners.com/customer-supplier -->

<!-- Partnership : https://ddd-practitioners.com/partnership -->

<!-- Conformist : https://ddd-practitioners.com/conformist -->
<!-- Anti-Corruption Layer (ACL) : https://ddd-practitioners.com/anticorruption-layer -->
<!-- Test-Driven Development : https://ddd-practitioners.com/test-driven-development -->
[[Test-Driven Development]] TDD is a lightweight programming methodology that emphasizes fast, incremental development and especially writing tests before writing code. Ideally these follow one another in cycles measured in minutes. (see full definition under [[Test-Driven Development]] topic)

<!-- Open-Host Service : https://ddd-practitioners.com/open-host-service -->

<!-- Shared Kernel : https://ddd-practitioners.com/shared-kernel -->

<!-- Published Language : https://ddd-practitioners.com/published-language -->

<!-- Layered Architecture : https://ddd-practitioners.com/layered-architecture -->
<!-- [[Layered Architecture]] A technique for separating the concerns of a software system, isolating a domain layer, among other things. -->

<!-- Infrastructure Service : https://ddd-practitioners.com/infrastructure-service -->

<!-- Domain Services: https://ddd-practitioners.com/home/glossary/domain-services -->
<!-- Application Service : https://ddd-practitioners.com/application-service -->

<!-- Ubiquitous Language : https://ddd-practitioners.com/home/glossary/ubiquitous-language -->
<!-- [[Ubiquitous Language]] A language structured around the domain model and used by all team members to connect all the activities of the team with the software. -->

<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@saga -->
<!--@CQRS (Command Query Responsibility Segregation): -->
<!--@Event Sourcing: -->
<!-- Strong Consistency : https://ddd-practitioners.com/?page_id=421 -->
<!-- Snapshots : https://ddd-practitioners.com/snapshots -->
<!-- Saga : https://ddd-practitioners.com/home/glossary/saga -->
<!-- Outbox Pattern -->
<!-- Optimistic Concurrency Control : https://ddd-practitioners.com/?page_id=609 -->

<!-- https://www.linkedin.com/pulse/api-strategy-conways-law-inverse-conway-manoeuvre-mikael-wall%C3%A9n/ -->

Một mô hình lưu trữ dữ liệu, trong đó tất cả các thay đổi trạng thái của hệ thống được biểu diễn dưới dạng sự kiện (event).

<!-- EventStorming : https://ddd-practitioners.com/home/glossary/eventstorming -->
<!-- Domain Storytelling : https://ddd-practitioners.com/?page_id=1005 -->

<!-- CQRS : https://ddd-practitioners.com/?page_id=574 -->

CQRS chia để thoải mái, chặt chẽ

Là một nguyên tắc trong DDD, CQRS tách biệt giữa phần xử lý câu lệnh (Command) và phần truy vấn dữ liệu (Query).
Command đại diện cho các thao tác cập nhật dữ liệu, trong khi Query đại diện cho các thao tác truy vấn dữ liệu.

<!-- Event-Driven Architecture : https://ddd-practitioners.com/home/glossary/event-driven-architecture -->

<!-- Event Modeling : https://ddd-practitioners.com/?page_id=994 -->

<!-- Event Replay : https://ddd-practitioners.com/?page_id=585 -->

<!-- Event Sourced Aggregates : https://ddd-practitioners.com/event-sourcing -->

<!-- Event Sourcing : https://ddd-practitioners.com/?page_id=581 -->

<!-- Eventual Consistency : https://ddd-practitioners.com/?page_id=419 -->

<!-- Change Data Capture: https://en.wikipedia.org/wiki/CAP_theorem -->

<!-- ACID Transaction : https://ddd-practitioners.com/?page_id=415 -->

ACID (Atomicity, Consistency, Isolation, Durability)

<!-- BASE Transaction -->

BASE là viết tắt của "Basically Available, Soft state, Eventually consistent," và đối lập với ACID

<!-- Command : https://ddd-practitioners.com/?page_id=596 -->
<!-- Command Handler : https://ddd-practitioners.com/?page_id=599 -->
<!-- Compensating Action : https://ddd-practitioners.com/compensating-action -->
<!-- Compensating Transaction : https://ddd-practitioners.com/compensating-transaction -->
<!-- Compensating Workflow : https://ddd-practitioners.com/compensating-workflow -->

<!-- Domain Event : https://ddd-practitioners.com/domain-event -->
<!-- PublishSubscribe : https://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html -->
<!--@ Dependency Inversion Principle -->

SOLID : https://ddd-practitioners.com/home/glossary/solid
Single Responsibility Principle : https://ddd-practitioners.com/single-responsibility-principle
Open-Closed Principle
Liskov Substitution Principle : https://ddd-practitioners.com/home/glossary/liskov-substitution-principle
Interface Segregation Principle : https://ddd-practitioners.com/?page_id=817

<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!--!========================================================== -->
<!-- mỗi dịch vụ xuất bản và đăng ký các sự kiện nếu cần. Cách tiếp cận này có thể mở rộng và linh hoạt hơn so với điều phối, nhưng cũng phức tạp hơn trong việc triển khai và bảo trì. Tuy nhiên, nó cũng có thể linh hoạt hơn vì mỗi dịch vụ có thể phát triển độc lập và lỗi trong một dịch vụ không nhất thiết ảnh hưởng đến toàn bộ hệ thống. -->

<!-- -->

<!-- -->

[[Analysis Pattern]] A group of concepts that represents a common construction in business modeling. It may be relevant to only one domain or may span many domains (Fowler 1997, p. 8).

[[Assertion]] A statement of the correct state of a program at some point, independent of how it does it. Typically, an ASSERTION specifies the result of an operation or an invariant of a design element.

[[Bounded Context]] The delimited applicability of a particular model. BOUNDING CONTEXTS gives team members a clear and shared understanding of what has to be consistent and what can develop independently.

[[Client]] A program element that is calling the element under design, using its capabilities.

[[Cohesion]] Logical agreement and dependence.

[[Command]] (a.k.a. modifier) An operation that effects some change to the system (for example, setting a variable). An operation that intentionally creates a side effect.

[[Conceptual Contour]] An underlying consistency of the domain itself, which, if reflected in a model, can help the design accommodate change more naturally.

[[Declarative Design]] A form of programming in which a precise description of properties actually controls the software. An executable specification.

[[Design Pattern]] A description of communicating objects and classes that are customized to solve a general design problem in a particular context. (Gamma et al. 1995, p. 3)

[[Distillation]] A process of separating the components of a mixture to extract the essence in a form that makes it more valuable and useful. In software design, the abstraction of key aspects in a model, or the partitioning of a larger system to bring the CORE DOMAIN to the fore.

<!-- [[Domain Layer]] That portion of the design and implementation responsible for domain logic within a LAYERED ARCHITECTURE. The domain layer is where the software expression of the domain model lives. -->

[[Function]] An operation that computes and returns a result without observable side effects.

[[Immutable]] The property of never changing observable state after creation. implicit concept A concept that is necessary to understand the meaning of a model or design but is never mentioned.

[[Intention-Revealing Interface]] A design in which the names of classes, methods, and other elements convey both the original developer’s purpose in creating them and their value to a client developer.

[[Invariant]] An Assertion about some design element that must be true at all times, except during specifically transient situations such as the middle of the execution of a method, or the middle of an uncommitted database transaction.

[[Iteration]] A process in which a program is repeatedly improved in small steps. Also, one of those steps.

[[Large-Scale Structure]] A set of high-level concepts, rules, or both that establishes a pattern of design for an entire system. A language that allows the system to be discussed and understood in broad strokes.

<!-- [[Model-Driven Design]] A design in which some subset of software elements corresponds closely to elements of a model. Also, a process of codeveloping a model and an implementation that stay aligned with each other. -->

[[Modeling Paradigm]] A particular style of carving out concepts in a domain, combined with tools to create software analogs of those concepts (for example, object-oriented programming and logic programming).

[[Responsibility]] An obligation to perform a task or know information (Wirfs-Brock et al. 2003, p. 3).

[[Side Effect]] Any observable change of state resulting from an operation, whether intentional or not, even a deliberate update.

[[Side Effect Free Function]] See [[Function]].

[[Standalone Class]] A class that can be understood and tested without reference to any others, except system primitives and basic libraries.

[[Stateless]] The property of a design element that allows a client to use any of its operations without regard to the element’s history. A stateless element may use information that is accessible globally and may even change that global information (that is, it may have side effects) but holds no private state that affects its behavior.

[[Supple Design]] A design that puts the power inherent in a deep model into the hands of a client developer to make clear, flexible expressions that give expected results robustly. Equally important, it leverages that same deep model to make the design itself easy for the implementer to mold and reshape to accommodate new insight.

[[Unification]] The internal consistency of a model such that each term is unambiguous and no rules contradict.

[[Whole Value]] An object that models a single, complete concept.
